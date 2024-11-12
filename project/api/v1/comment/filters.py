from django_filters import FilterSet, UUIDFilter


class CommentFilter(FilterSet):
    """
    Возвращает комментарии согласно фильтрации

    по uuid пользователя
    /api/v1/comment/?author=
    """

    author = UUIDFilter(field_name="author")
    task = UUIDFilter(field_name="task")
