from ex1.mapping import RAW_MAPPING


def build_roles_tree(mapping):
    """
    :param mapping: маппинг ролей в категории
    :return: дерево ролей
    """
    # put your code here
    result = list(map(lambda category: {
            'id': 'category-' + mapping['categories'][category]['id'],
            'text': mapping['categories'][category]['name'],
            'items': list(map(lambda role: {
                'id': mapping['roles'][role]['id'],
                'text': mapping['roles'][role]['name']
            }, mapping['categories'][category]['roleIds']))
        }, mapping['categoryIdsSorted']
    ))
    return {'categories': result}