bl_info = {
    "name": "Object Adder",
    "author": "dvd",
    "version": (1, 0),
    "blender": (2, 90, 0),  # Development version
    "location": "View 3D > Tool Shelf",
    "warning": "",
    "wiki_url": "You can write the GitHub URL here",
    "category": "Check the plugin category list, the URL is here: https://docs.blender.org/manual/en/4.1/addons/index.html ",
}
# Basic information

import bpy

# My Panel is the name, can be changed freely
class MyPanel(bpy.types.Panel):
    bl_label = "Name, for example MyPanel"
    bl_idname = "VIEW3D_PT_my_panel"  # Used to connect sub-panels
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'  # Refers to the 3D view, side toolbar
    bl_category = "MyPanel"
    # This defines the main panel, the name and position displayed in the sidebar. If set to 'tool', it will be found under 'tool' menu
    # if the sidebar does not have it, a new tab with this name will be created.
    #! This "category" determines whether it is under a certain page or creates a new page.

    def draw(self, context):  # Define, as starting to draw a panel
        layout = self.layout  # Get the current panel's layout, necessary
        
        layout.label(text="Hello, World!")  # Plain text; for icons,just add,icon=""
        row = layout.row()  # Create a new row
        row.operator("object.simple_operator")  # Call operator,can be either blender operator or self written operator
        
        row = layout.row()
        row.operator("mesh.primitive_uv_sphere_add", icon='SPHERE')
        # Icon; you can also add something such as, text="add a sphere"

class SimpleOperator(bpy.types.Operator):
    bl_idname = "object.simple_operator"  # Name to be called
    bl_label = "Click Me"  # The text displayed on the button when there's no text

    def execute(self, context):
        self.report({'INFO'}, "Button Clicked!")
        return {'FINISHED'}

class PanelA(bpy.types.Panel):
    bl_label = "Panel A"
    bl_idname = "A_TestPanel"
    # The following three are the panel's location information
    bl_space_type = "VIEW_3D"
    bl_region_type = 'UI'
    bl_category = 'My First Addon'
    bl_parent_id = "VIEW3D_PT_my_panel"
    # Adding this will indent this panel, if the parent_id if from the main panel
    bl_options = {'DEFAULT_CLOSED'}
    # The small panel is collapsed by default
    
    def draw(self, context):
        # Draw a panel
        layout = self.layout
        
        row = layout.row()
        row.label(text="Panel A is here", icon='FONT_DATA') 
        # Label is an explanation, just text and icon, no function
        row = layout.row()
        row.operator("transform.resize")
        # The operator in the parentheses can be replaced with other operators
        layout.scale_y = 1.4  # Only y works, adjusting the vertical scale
        # row →, column ↓
        col = layout.column()
        col.prop(context.object, "scale")
        col = layout.column()
        col.operator("object.modifier_add") 
        col.operator("object.subdivision_set", icon='MOD_SMOOTH', text="SubD")
        col.operator("mesh.popup_window")
        
from bpy.props import EnumProperty, FloatProperty

# * Operator that will show a popup  
class MESH_OT_popup_window(bpy.types.Operator):
    bl_idname = "mesh.popup_window"
    bl_label = "Create Shape"
    bl_options = {'REGISTER', 'UNDO'}
    
    # Choose between a cube or a sphere    
    shape_type: EnumProperty(
        name="Shape",
        description="Choose the shape to create",
        items=[
            ('CUBE', "Cube", "Create a cube"),
            ('SPHERE', "Sphere", "Create a UV Sphere")
        ]
    )
    
    # Scale
    scale: FloatProperty(
        name="Scale",
        description="Scale of the shape",
        default=1.0,
        min=0.1,
        max=10.0
    )
    
    # Invoke the window
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
    
    # Selection
    def execute(self, context):
        if self.shape_type == 'CUBE':
            bpy.ops.mesh.primitive_cube_add(scale=(self.scale, self.scale, self.scale))
        elif self.shape_type == 'SPHERE':
            bpy.ops.mesh.primitive_uv_sphere_add(radius=self.scale)
        return {'FINISHED'}

def register():
    # Register; fill in the class names in parentheses
    bpy.utils.register_class(MyPanel)
    bpy.utils.register_class(SimpleOperator)
    bpy.utils.register_class(PanelA)
    bpy.utils.register_class(MESH_OT_popup_window)

def unregister():
    bpy.utils.unregister_class(MyPanel)
    bpy.utils.unregister_class(SimpleOperator)
    bpy.utils.unregister_class(PanelA)
    bpy.utils.unregister_class(MESH_OT_popup_window)

if __name__ == "__main__":
    register()
