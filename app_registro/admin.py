from django.contrib import admin
from .models import Asistencia, Conferencia, Conferencista, Participante

# ------------------------------------------------------------------------
class ConferenciaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'fecha', 'hora',)
    list_editable = ('nombre',)

admin.site.register(Conferencia, ConferenciaAdmin)
# ------------------------------------------------------------------------
admin.site.register(Conferencista)
# ------------------------------------------------------------------------
admin.site.register(Asistencia)
#-------------------------------------------------------------------------
admin.site.register(Participante)
