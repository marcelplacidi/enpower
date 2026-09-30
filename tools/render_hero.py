"""Render hero.png: 3D radiosity of SOLEY's furnished_office.dxf preset.

All sources on: both windows at 10 W/m2 at the glass and the eight ceiling panels
at the import default (3600 lm). A 5 x 5 cm CZTS cell lies on the desk in front of
the left window. Each solved patch is painted with its own radiosity (no smoothing),
following docs/onepager_insoley/make_figures.py in the SOLEY repo. Run from anywhere:
    python tools/render_hero.py
Outputs assets/img/hero.png and tools/hero_run.json (cell irradiance and power).
"""
import os, sys, json, logging

SOLEY = r"C:\dev\SOLEY"
OUT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def ok(label, r):
    if isinstance(r, dict) and r.get("error"):
        raise RuntimeError(f"{label}: {r.get('code')} - {r.get('message')}")
    return r


CELL_POS = [2.0, 5.0, 0.80]   # on the left desk top (z1 = 0.75 m)
CELL_SIDE = 0.05              # m
WIN_PD = 10.0                 # W/m2 at the window


def main():
    os.chdir(SOLEY)
    sys.path.insert(0, SOLEY)
    import numpy as np
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.colors import LinearSegmentedColormap, LogNorm
    from mpl_toolkits.mplot3d.art3d import Poly3DCollection
    from html_gui.backend.api import SOLEYAPI
    logging.getLogger("soley.api").setLevel(logging.ERROR)

    api = SOLEYAPI()
    ok("core", api.load_project({"filepath": r"presets\configurations\czts.soley"}))
    ok("cad", api.import_insoley3d_cad({"filepath": r"presets\room3d\furnished_office.dxf",
                                        "ceilingHeight": 2.8, "unitsToM": 1.0,
                                        "windowSill": 0.9, "windowHead": 2.1,
                                        "objectAlbedo": 0.5}))
    ok("conn", api.connect_insoley_to_soley())
    scene = ok("scene", api.get_insoley3d_scene({}))["scene"]
    for w in scene["windows"]:
        ok("win", api.set_insoley3d_window({"id": w["id"], "windowPowerDensity": WIN_PD,
                                            "daylightPreset": ""}))
    for lamp in scene["lightSources"]:
        ok("lamp", api.set_insoley3d_lamp({"id": lamp["id"], "luminousFlux": 3600.0}))
    ok("mask", api.set_insoley3d_source_mask({"mask": "all"}))
    ok("cell", api.set_insoley3d_cell({"position": CELL_POS, "tilt": 0.0, "azimuth": 0.0,
                                       "area": CELL_SIDE ** 2}))
    run = ok("run", api.run_insoley3d_simulation({"operatingHours": 1.0}))
    dev = run["device"]
    pt = ok("pt", api.get_insoley3d_point_spectrum({"position": CELL_POS, "tilt": 0.0,
                                                    "azimuth": 0.0}))
    summary = {"window_power_density_Wm2": WIN_PD,
               "cell_irradiance_Wm2": pt.get("irradiance_Wm2"),
               "device": {k: dev.get(k) for k in ("powerDensityCell_Wm2", "power_mW",
                                                   "efficiencyPct", "jsc", "voc", "ff")}}
    with open(os.path.join(OUT_DIR, "tools", "hero_run.json"), "w") as f:
        json.dump(summary, f, indent=2, default=float)
    print(json.dumps(summary, indent=2, default=float))

    # Patch geometry + radiosity from the same cached simulator the API uses.
    p, sc = api._require_scene()
    sim = api._scene_simulator(sc, p.export_wavelengths)
    B = np.asarray(api._radiosity_field(sim), dtype=float)
    patches = sim.rad.patches

    # Cutaway: drop the ceiling and the two walls facing the camera (y=0 and x=8).
    def keep(pch):
        return pch.vertices is not None and pch.surface_type not in ("ceiling", "wall:0", "wall:1")

    idx = [i for i, pch in enumerate(patches) if keep(pch)]
    vals_all = B[idx]
    floor = np.percentile(vals_all[vals_all > 0], 3)
    norm = LogNorm(vmin=floor, vmax=vals_all.max())
    cmap = LinearSegmentedColormap.from_list(
        "enpower", ["#14181f", "#26344a", "#4f6680", "#a3a9a6", "#e2d6b8", "#fbf6ea"])

    light = np.array([-0.35, -0.55, 0.76]); light /= np.linalg.norm(light)
    groups = {"floor": [], "wall": [], "object": []}
    for i in idx:
        pch = patches[i]
        c = np.array(cmap(norm(max(B[i], floor))))
        if not (pch.surface_type == "floor" or pch.surface_type.startswith("wall")):
            c[:3] *= 0.88 + 0.12 * max(0.0, float(np.dot(pch.normal, light)))
        g = "floor" if pch.surface_type == "floor" else ("wall" if pch.surface_type.startswith("wall") else "object")
        groups[g].append((np.asarray(pch.vertices, float), c))

    fig = plt.figure(figsize=(14, 10), dpi=200)
    ax = fig.add_axes([0, 0, 1, 1], projection="3d")
    ax.computed_zorder = False
    for z, g in enumerate(("floor", "wall", "object"), start=1):
        qs = [q for q, _ in groups[g]]; cs = [c for _, c in groups[g]]
        col = Poly3DCollection(qs, facecolors=cs, edgecolors=cs, linewidths=0.25, shade=False)
        col.set_zsort("average")
        col.set_zorder(z)
        ax.add_collection3d(col)

    # Windows: pale glazing outline on the back wall.
    walls = {w["id"]: w for w in scene["walls"]}
    for w in scene["windows"]:
        wall = walls[w["wallId"]]
        p0, p1 = np.array(wall["p0"]), np.array(wall["p1"])
        a, b = p0 + w["u0"] * (p1 - p0), p0 + w["u1"] * (p1 - p0)
        y = a[1] - 0.01
        quad = [[a[0], y, w["z0"]], [b[0], y, w["z0"]], [b[0], y, w["z1"]], [a[0], y, w["z1"]]]
        wc = Poly3DCollection([quad], facecolors=(1, 1, 1, 0.12),
                              edgecolors="#ffffff", linewidths=1.6)
        wc.set_zorder(2.5)
        ax.add_collection3d(wc)

    # PV cell: true size, dark absorber with a green frame, plus a leader and label.
    cx, cy, cz = CELL_POS
    h = CELL_SIDE / 2
    cell = [[cx - h, cy - h, cz + 0.01], [cx + h, cy - h, cz + 0.01],
            [cx + h, cy + h, cz + 0.01], [cx - h, cy + h, cz + 0.01]]
    for k, a in ((0.30, 0.14), (0.20, 0.26), (0.12, 0.45)):
        halo = [[cx - k, cy - k, cz + 0.005], [cx + k, cy - k, cz + 0.005],
                [cx + k, cy + k, cz + 0.005], [cx - k, cy + k, cz + 0.005]]
        hc = Poly3DCollection([halo], facecolors=(0.784, 0.255, 0.169, a), edgecolors="none")
        hc.set_zorder(9)
        ax.add_collection3d(hc)
    cc = Poly3DCollection([cell], facecolors="#0d1b2a", edgecolors="#c8412b", linewidths=2.4)
    cc.set_zorder(10)
    ax.add_collection3d(cc)
    ln, = ax.plot([cx, cx], [cy - 0.05, cy - 0.05], [cz + 0.03, cz + 1.75], color="#c8412b", lw=1.4)
    ln.set_zorder(11)
    dot = ax.scatter([cx], [cy - 0.05], [cz + 1.75], color="#c8412b", s=26)
    dot.set_zorder(11)
    tx = ax.text(cx - 0.12, cy - 0.05, cz + 1.75, "indoor PV cell", color="#14181f",
                 fontsize=18, ha="right", va="center", family="DejaVu Sans")
    tx.set_zorder(12)

    ax.set_xlim(0, 8); ax.set_ylim(0, 6); ax.set_zlim(0, 2.8)
    ax.set_box_aspect((8, 6, 2.8))
    ax.view_init(elev=30, azim=-58)
    ax.set_axis_off()
    fig.patch.set_alpha(0); ax.patch.set_alpha(0)
    out = os.path.join(OUT_DIR, "assets", "img", "hero_raw.png")
    fig.savefig(out, transparent=True, dpi=200)
    print("saved", out)
    # Tight crop on the drawn pixels, a small margin kept, written as hero.png.
    from PIL import Image
    im = Image.open(out)
    l, t, r, b = im.getbbox()
    m = 40
    im.crop((max(l - m, 0), max(t - m, 0), min(r + m, im.width), min(b + m, im.height))).save(
        os.path.join(OUT_DIR, "assets", "img", "hero.png"), optimize=True)
    os.remove(out)
    print("saved hero.png")


if __name__ == "__main__":
    main()
