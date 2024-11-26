from rest_framework.permissions import BasePermission
VIEW_METHODS = ['GET', 'OPTIONS', 'HEAD']
CHANGE_METHODS = ['PUT', 'PATCH']
class GlobalDefaultPermission(BasePermission):
    #FUNÇÃO PARA RETORNAR A PERMISSÃO DO USUARIO (APP.METHOD_MODEL)
    def has_permission(self, request, view):
        model_permission_codename = self.__get_model_permission_codename(
            method=request.method,
            view=view
        )
        if not model_permission_codename:
            return False
        
        return request.user.has_perm(model_permission_codename)

    #FUNÇÃO QUE IRÁ PEGAR O NOME DE APP, NOME DA MODEL E TIPO DE METHOD
    def __get_model_permission_codename(self, method, view):
        try:
            model_name = view.queryset.model._meta.model_name #PEGA O NOME DO MODEL
            app_label = view.queryset.model._meta.app_label #PEGA O NOME DA APP (PASTA)
            action = self.__get_action(method) #PEGA O NOME DA PERMISSÃO COM BASE NA METHOD DA REQUISIÇÃO
            return f'{app_label}.{action}_{model_name}'
        except AttributeError:
            return None
    #FUNÇÃO PARA PEGAR O METHOD DA REQUISIÇÃO
    def __get_action(self, method):
        method_action = {
            'GET': 'view',
            'OPTIONS': 'view',
            'HEAD': 'view',
            'POST': 'add',
            'PUT': 'change',
            'PATCH': 'change',
            'DELETE': 'delete'
        }
        return method_action.get(method, '')