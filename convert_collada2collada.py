import sys; sys.path.append(".")
from modules.argument_parser_for_blender import ArgumetParserForBlender

import bpy
import pathlib


def collada2stl(input_dir):
    p = pathlib.Path(input_dir)
    collada_files = list(p.glob("**/*.dae"))

    for collada in collada_files:
        bpy.ops.object.select_all(action="DESELECT")
        bpy.ops.object.select_all(action="SELECT")
        bpy.ops.object.delete()

        bpy.ops.wm.collada_import(filepath=collada.as_posix())
        bpy.ops.object.select_all(action="DESELECT")
        bpy.ops.object.select_all(action="SELECT")

        # 90 deg rotation
        bpy.context.object.rotation_euler[0] = 0

        bpy.ops.wm.collada_export(filepath=collada.as_posix())


if __name__ == "__main__":
    parser = ArgumetParserForBlender()
    parser.add_argument("collada_dir", type=str)

    args = parser.parse_args()

    collada_dir = args.collada_dir

    collada2stl(collada_dir)
