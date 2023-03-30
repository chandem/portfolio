from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField, TextAreaField, DateTimeField,BooleanField
from wtforms.validators import DataRequired, Length, Email, ValidationError

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=64)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')

class WorkOrderForm(FlaskForm):
    asset_id = IntegerField('Asset ID', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired(), Length(max=255)])
    priority = SelectField('Priority', choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], validators=[DataRequired()])
    status = SelectField('Status', choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed')], validators=[DataRequired()])
    assigned_to = StringField('Assigned To', validators=[Length(max=64)])
    start_date = DateTimeField('Start Date', format='%Y-%m-%d %H:%M:%S')
    end_date = DateTimeField('End Date', format='%Y-%m-%d %H:%M:%S')
    inspection_id = IntegerField('Inspection ID')
    submit = SubmitField('Create Work Order')

class InspectionForm(FlaskForm):
    asset_id = IntegerField('Asset ID', validators=[DataRequired()])
    inspector = StringField('Inspector', validators=[DataRequired(), Length(max=64)])
    inspection_date = DateTimeField('Inspection Date', format='%Y-%m-%d %H:%M:%S', validators=[DataRequired()])
    condition = StringField('Condition', validators=[DataRequired(), Length(max=64)])
    notes = TextAreaField('Notes', validators=[Length(max=255)])
    submit = SubmitField('Create Inspection')

class AssetForm(FlaskForm):
    asset_type = StringField('Asset Type', validators=[DataRequired(), Length(max=64)])
    location = StringField('Location', validators=[DataRequired(), Length(max=255)])
    condition = StringField('Condition', validators=[DataRequired(), Length(max=64)])
    last_inspection_date = DateTimeField('Last Inspection Date', format='%Y-%m-%d %H:%M:%S')
    submit = SubmitField('Create Asset')