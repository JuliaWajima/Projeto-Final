from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField, TextAreaField
from wtforms.validators import DataRequired,Email,EqualTo,ValidationError, Length
from app import db,bcrypt
from app.models import User


class Userform(FlaskForm):
    nome=StringField('Nome',validators=[DataRequired()])
    email=StringField('E-mail',validators=[DataRequired(),Email()])
    senha=PasswordField('Senha',validators=[DataRequired()])
    confirmacao_senha=PasswordField('Confirme sua senha',validators=[DataRequired(),EqualTo('senha')])
    btnSubmit=SubmitField('Cadastrar')

    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError('Usuário já cadastrado com esse Email >:(')
    def save(self):
        senha = bcrypt.generate_password_hash(self.senha.data).decode('utf-8')
        user=User(
            nome=self.nome.data,
            email=self.email.data,
            senha=senha
        )
        db.session.add(user)
        db.session.commit()
        return user


class LoginForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    btnSubmit = SubmitField('Login')
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if not user:
            raise ValidationError('Usuário não encontrado :(')
        
    def validate_senha(self, senha):
        user = User.query.filter_by(email=self.email.data).first()
        if not user or not bcrypt.check_password_hash(user.senha, senha.data.encode('utf-8')):
            raise ValidationError('Senha errada :(')

        
