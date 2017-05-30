import bpy
import os
from bpy.types import Panel
from bpy import context

bl_info = {"name": "One Click Export Addon", "category": "Object"}

class OneExport(bpy.types.Operator):
	bl_idname = "one.export"
	bl_label = 'One Click Export'
	bl_description = 'Use This Button To Export Models From Blender With A Single Click'
	bl_options = {'REGISTER', 'UNDO'}
	
	Location = bpy.props.StringProperty(name='Location')
	Name = bpy.props.StringProperty(name='Name')
	
	def execute(self, context):
		message = "Export: '%s'" % \
			(self.Location)
		self.report({'INFO'}, message)
		#Get The Directory To Export The File To
		ExportPath = self.Location
		
		#Set The Name Of The File
		Name = self.Name + '.fbx'
		
		#Combine The Export Path And Name Together To Export The File
		bpy.ops.export_scene.fbx(filepath = ExportPath + Name,use_selection = True)
		return('FINISHED')
		
	def invoke(self, context, event):
		#Create The PopUp Window To Enable User To Input File Name And Location
		wm = context.window_manager
		return wm.invoke_props_dialog(self)
		
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
		layout.operator("one.export",text='Export',icon='QUESTION')
	
def register():
	bpy.utils.register_class(OneExport)
	bpy.utils.register_class(OneClickPanel)
	
def unregister():
	bpy.utils.unregister_class(OneExport)
	bpy.utils.unregister_class(OneClickPanel)
	
if __name__ == '__main__':
	register()