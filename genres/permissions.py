from rest_framework.permissions import BasePermission
HTTP_REQUISITIONS = ('GET', 'OPTIONS', 'HEAD')
class GenrePermissionClass(BasePermission):

    def has_permission(self, request, view):
        match request.method:
            case method if method in HTTP_REQUISITIONS:
                return request.user.has_perm('genres.view_genre')
            case 'POST':
                return request.user.has_perm('genres.add_genre')
            case 'PUT':
                return request.user.has_perm('genres.change_genre')
            case 'DELETE':
                return request.user.has_perm('genres.delete_genre')
            case _:
                return False
        