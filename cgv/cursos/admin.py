from django.contrib import admin

from cursos.models import Ciclo, Curso


class CicloAdmin(admin.ModelAdmin):
	pass


class CursoAdmin(admin.ModelAdmin):
	pass

	


admin.site.register(Ciclo, CicloAdmin)
admin.site.register(Curso, CursoAdmin)