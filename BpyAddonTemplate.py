bl_info = {
    "name":"Object Adder",
    "author":"dvd",
    "version":(1,0),
    "blender":(2,90,0), #开发版本
    "location":"View 3D > Tool Shelf",
    "warning":"",
    "wiki_url":"可以写github_url",
    "category":"这里去看一下插件类别列表, url在此:https://docs.blender.org/manual/en/4.1/addons/index.html ",
}
#基础信息

import bpy

#My Panel是名字, 可以任意改
class MyPanel(bpy.types.Panel):
    bl_label = "名字,比如MyPanel"
    bl_idname = "VIEW3D_PT_my_panel"    #用来连接子panel的
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI' #指3dview, 侧边工具栏
    bl_category = "MyPanel"
    #这里是主导面板的, 在侧边栏显示的名字和位置, 要是填tool就会在tool下找到, 要是侧栏没有那就会多一个标签显示这里的名字
    #! 这个category决定了是在某个页下面, 还是新创一个页

    def draw(self, context): #定义, 可以理解为开始画一个panel
        layout = self.layout #获取当前面板的布局对象,是必要的
        
        layout.label(text="Hello, World!") #纯文字, 要是要图标则 ,icon=""
        row = layout.row() #创建新行
        row.operator("object.simple_operator") #调用operator
        
        row = layout.row()
        row.operator("mesh.primitive_uv_sphere_add",icon='SPHERE')
        #icon是图标, 需要的话可以在加类似 text="add a sphere" 这种
        

class SimpleOperator(bpy.types.Operator):
    bl_idname = "object.simple_operator"#被调用的名字
    bl_label = "Click Me"#按钮在没有text的情况下, 显示的字

    def execute(self, context):
        self.report({'INFO'}, "Button Clicked!")
        return {'FINISHED'}

class PanelA(bpy.types.Panel):
    bl_label = "Panel A"
    bl_idname = "A_TestPanel"
    #以下三个是panel会加的, 位置信息
    bl_space_type = "VIEW_3D"
    bl_region_type = 'UI' #特指在ctrl+T/T摁出来的侧边栏
    bl_category = 'My First Addon'
    bl_parent_id = "VIEW3D_PT_my_panel"
    #主面板是Mypanel的话,加了这个以后会让这一条面板缩进
    bl_options = {'DEFAULT_CLOSED'}
    #小页面默认不展开
    
    def draw(self, context):
        #画一个面板
        layout = self.layout
        
        row = layout.row()
        row.label(text= "Panel A is herer", icon='FONT_DATA') 
        #label是说明, 只是文字和图标, 没有功能
        row = layout.row()
        row.operator("transform.resize")
        #这里的operator括号里的, 可以替换成其他的, 比如有自己def的函数operator的class()
        layout.scale_y = 1.4 #only y works, adjusting the verticle scale
        #row →, column↓
        col = layout.column()
        col.prop(context.object, "scale")
        col = layout.column()
        col.operator("object.modifier_add") 
        col.operator("object.subdivision_set", icon='MOD_SMOOTH', text="SubD")
        col.operator("mesh.popup_window")
        
        

#*会出现弹窗的Operator  
class MESH_OT_popup_window(bpy.types.Operator):
    bl_idname = "mesh.popup_window"
    bl_label = "Create Shape"
    bl_options = {'REGISTER', 'UNDO'}
    
    #选择方块还是球体    
    shape_type: EnumProperty(
        name="Shape",
        description="Choose the shape to create",
        items=[
            ('CUBE', "Cube", "Create a cube"),
            ('SPHERE', "Sphere", "Create a UV Sphere")
        ]
    )
    
    #缩放
    scale: FloatProperty(
        name="Scale",
        description="Scale of the shape",
        default=1.0,
        min=0.1,
        max=10.0
    )
    
    #唤出窗口
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
    
    #选择
    def execute(self, context):
        if self.shape_type == 'CUBE':
            bpy.ops.mesh.primitive_cube_add(scale=(self.scale, self.scale, self.scale))
        elif self.shape_type == 'SPHERE':
            bpy.ops.mesh.primitive_uv_sphere_add(radius=self.scale)
        return {'FINISHED'}


def register():
    #注册, 括号里填class的名字
    bpy.utils.register_class(MyPanel)
    bpy.utils.register_class(SimpleOperator)
    bpy.utils.register_class(PanelA)
    bpy.utils.register_class(MESH_OT_popup_window)

def unregister():
    bpy.utils.unregister_class(MyPanel)
    bpy.utils.unregister_class(SimpleOperator)
    bpy.utils.unregister_class(PanelA)
    bpy.utils.register_class(MESH_OT_popup_window)

if __name__ == "__main__":
    register()
