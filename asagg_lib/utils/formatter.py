def format_attributes_names(
    attributes: list[str], classname: str = ""
) -> list[str]:
    """
    Format attributes to make a new attribute and remove classname if attribute name contains it

    Parameters:
         attributes: list of all attribute that you want format
         classname: name of class that you retrive the attributes
    Returns:
        return all attributes formatted to make new public attributes

    Examples:
        >>> format_attributes_names(["_foo", "_Square_foo"], "Square")
        ['foo', 'foo']
    """
    attributes_formatted: list[str] = []
    for attr in attributes:
        attr = attr.replace("_", "")
        if classname in attr:
            attr = attr.replace(classname, "")
        attributes_formatted.append(attr)

    return attributes_formatted
