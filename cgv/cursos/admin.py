from django.contrib import admin

from cursos.models import Ciclo, Curso


class CicloAdmin(admin.ModelAdmin):
	pass


class CursoAdmin(admin.ModelAdmin):
	
	class Media:
		js = [
			'admin/js/tinymce/tinymce.min.js',
			'admin/js/tinymce/config.js',
		]
	


admin.site.register(Ciclo, CicloAdmin)
admin.site.register(Curso, CursoAdmin)