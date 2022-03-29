# Workflow

## Preparation:
1. Rest armature should have only transitions in skeleton, no rotation, no stretching, bone head/tail should keep their places.
2. Weights need to be normalized.
3. Head should be exported with root in world origin.
4. Mesh (head and body) should be bound to human armature, modifier applied, and then unwrapped back via animation in CK3.

## Animation:
1. Use NLA action in Blender to set up default pose to unwrap deformed mesh.
2. Disable head export action for animation and body export.
3. Do animation.
4. Export body animation.
5. Enable head export action to reset head root at the world origin.
6. Export body animation.