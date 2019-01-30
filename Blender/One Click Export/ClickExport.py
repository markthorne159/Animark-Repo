import bpy
import os
from bpy.types import Panel
from bpy import context
from bpy.props import BoolProperty, StringProperty

bl_info = {"name": "One Click Export Addon", "category": "Object"}
#Set 'FBX' as initial filetype to export as.
bpy.context.scene["Type"] = ".fbx"

#Create boolean variable to be used to determine whether or not to export selected object.
bpy.types.Scene.Selection_bool = BoolProperty(
					name = 'Selection On Off',
					description = 'Selection checkbox',
					default = False)

class OneExport(bpy.types.Operator):
	bl_idname = "one.export"
	bl_label = 'One Click Export'
	bl_description = 'Use this button to set an export path.'
	bl_options = {'REGISTER', 'UNDO'}
	
	Location = bpy.props.StringProperty(name='Location')
	Name = bpy.props.StringProperty(name='Name')
	
	def execute(self, context):
		#Create custom property for Location.
		bpy.context.scene["LocA"] = self.Location
		print(bpy.context.scene["LocA"])
		#Create custom property for Name.
		bpy.context.scene["NameA"] = self.Name
		if(bpy.context.scene.Selection_bool == True):
			print("Selection!")
		
		return{'FINISHED'}
		
	def invoke(self, context, event):
		#Create The PopUp Window To Enable User To Input File Name And Location
		wm = context.window_manager
		return wm.invoke_props_dialog(self)
		Loc = self.Location

class Export_Func(bpy.types.Operator):
	bl_idname = 'export.func'
	bl_label = "Exporter"
	bl_description = 'Export function.'
	bl_options = {"REGISTER","UNDO"}
	
	def execute(self,context):
		#Get the value from the custom property.
		LocData = bpy.context.scene["LocA"]
		NameData = bpy.context.scene["NameA"]
		print(LocData)
		print(bpy.types.Scene.Selection_bool)
		#Create ExportPath string,combining object name,save location and "Selection" variable.
		ExportPath = LocData + "\\" + NameData + bpy.context.scene["Type"]
		print(ExportPath)
		#Export the file.
		bpy.ops.export_scene.fbx(filepath = ExportPath,use_selection = bpy.context.scene["Selection_bool"])
		return{'FINISHED'}
	
	
	
		
class OneClickPanel(Panel):
	bl_space_type = 'VIEW_3D'
	bl_region_type = 'TOOLS'
	bl_label = 'One Click Exporter'
	bl_context = 'objectmode'
	bl_category = 'One Click'
	
	#Draw The Panel
	def draw(self, context):
		layout = self.layout
		col = layout.column(align = True)
		scene = context.scene
		
		row = layout.row()
		row.label(text='One Click Exporter')
		layout.operator("one.export",text='Set path',icon='QUESTION')
		row = layout.row()
		layout.operator("export.func",text='Export',icon='QUESTION')
		row = layout.row()
		row.label("Use selection?")
		layout.prop(scene,"Selection_bool",text="Selection")
		row = layout.row()
		row.label('Set filetype')
	
def register():
	bpy.utils.register_class(OneExport)
	bpy.utils.register_class(Export_Func)
	bpy.utils.register_class(OneClickPanel)
	#Create a boolean property to turn on or off.
	#Also register boolean same as any other property.
	bpy.types.Scene.Selection_bool
	
def unregister():
	bpy.utils.unregister_class(OneExport)
	bpy.utils.register_class(Export_Func)
	bpy.utils.unregister_class(OneClickPanel)
	#Create a boolean property to turn on or off.
	#Also unregister boolean same as any other property.
	del bpy.types.Scene.Selection_bool
	
if __name__ == '__main__':
	register()
