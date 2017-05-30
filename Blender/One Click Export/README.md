### One Click Export Addon For Blender

I've spent a lot of time working in Blender and often found myself working on models for games that had to be tweaked and exported back into my project multiple times and after a while I started finding lenders built in export system to be a bit of a pain. While it works in the same way as exporting in most other programs I started to find it a little bit annoying having to go back through multiple screens in order to export the model after making a change that could sometimes be as simple as changing some normals.

To try and minimize the export process I came up with an idea, what if I could create a button which I could use to set the name of the file and the place I wanted it to be exported to and then use this button to export whatever I was working on with a single click? Thats where this addon comes in.

![ExampleA](https://puu.sh/w5IoB/fbe1025c94.png)

After installing the addon (Instructions for if you're new to installing addons are included below) simply press the "T" key to bring up the "Transform"  panel. You should now see a panel similar to the one shown above. Look along the left side of the panel for a that should be positioned underneath the navigation tab, which is labelled as "Naviga", clicking on this will open up a new tab with a button labelled export. Currently the addon only supports exporting the currently selected object so make sure the object you want to export is currently selected in the 3d viewport. With the object selected click the "Export" button. After clicking the button a small popup window will appear with two empty text boxes in. 

![EmptyTextBoxes](https://puu.sh/w5NqP/2a2cc0fdda.png)

The top one labelled "Location" is where you will need to type in, or copy and paste, the location that you want the file to be exported to. For a reason I don't quite understand Blender requires you to put an extra "\" at the end of the location you choose or else the export doesn't work (I'm currently working on adding an extra bit of code which will add this automatically). Underneath this is a second box labelled "Name" this box is for you to put in a name for your file. Once you click "Ok" Blender will export the file to your chosen destination. Keep an eye on the top right hand corner of the screen for a small box that appears in the header to tell you that the export has worked and a reminder of the location you sent the file to. 

