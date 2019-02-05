### One Click Export Addon For Blender

I've spent a lot of time working in Blender and often found myself working on models for games that had to be tweaked and exported back into my project multiple times and after a while I started finding Blenders built in export system to be a bit of a pain. While it works in the same way as exporting in most other programs I began finding it a little bit annoying having to go back through multiple screens in order to export the model after making a change that could sometimes be as simple as changing some normals or slightly extruding part of the mesh.

To try and minimize the export process I came up with an idea to see if I could develop a script/addon that would enable me to complete the export progress in a single click, which resulte in this addon.

Once the addon is installed pressing 'T' in object mode will open up the normal transform panel. At the bottom of the panel will be a new tab labelled "One Export". Clicking on this will dispaly a new set of options.

(Options image)

The first two buts are almost the most important ones. Clicking on the first one will open up a new window enabling you to set the destination you want the object to be exported to and what you want the file to be named. Clicking 'Ok' will then save these two details as their own custom property in Blender. The button below this is pretty self explanatory, clicking it will export the file to the chosen destination. The next option is a small checkbox, leaving this unchecked will cause everything in the scene to be exported when the 'Export' button is clicked. Alternatively clicking on the checkbox will mean that only the selected object gets exported.

