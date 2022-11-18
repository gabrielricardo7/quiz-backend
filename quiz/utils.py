from django.utils.html import format_html, format_html_join


def validadores_senha_txt_ajuda_html():
    """
    Retorna uma string HTML com todos os textos de ajuda
    de todos os validadores configurados em uma <ul>.
    """
    textos_ajuda = [
        "Sua senha não pode ser tão parecida com outras informações pessoais.",
        "Sua senha deve conter pelo menos 8 caracteres.",
        "Sua senha não pode ser uma senha comumente usada.",
        "Sua senha não pode ser totalmente numérica.",
    ]
    itens_ajuda = format_html_join(
        "", "<li>{}</li>", ((texto_ajuda,) for texto_ajuda in textos_ajuda)
    )
    return format_html("<ul>{}</ul>", itens_ajuda) if itens_ajuda else ""
