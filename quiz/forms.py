from .models import Pergunta
from .utils import validadores_senha_txt_ajuda_html
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
        ]
        labels = {
            'username': "Usuário",
        }
        help_texts = {
            'username': """
                * Máximo: 150 caracteres. Letras, dígitos e apenas @/./+/-/_.
            """,
        }
        error_messages = {
            'username': {
                'unique': "Um usuário com esse nome já existe.",
            }
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = "Senha"
        self.fields['password2'].label = "Confirmação de senha"

        self.fields['password1'].help_text = validadores_senha_txt_ajuda_html()
        self.fields[
            'password2'
        ].help_text = "Digite a mesma senha de antes, para verificação."

    error_messages = {
        'password_mismatch': "Os dois campos de senha não correspondem.",
    }


class NovaPergunta(ModelForm):
    class Meta:
        model = Pergunta
        fields = "__all__"
