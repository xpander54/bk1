tinymce.PluginManager.add('galeria', function(editor, url){


	editor.addButton('galeria', {
		text    : 'Galeria',
		icon    : false,
		onclick : function(){
			editor.windowManager.open({
				title    : 'Galeria',
				body     : [
					{type : 'textbox', name : 'prueba', label : 'Prueba'}
				],
				onsubmit : function(e){
					editor.insertContent('title:' + e.data.title);
				}
			});
		}
	});


});