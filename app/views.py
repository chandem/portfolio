from flask import render_template, redirect, url_for, flash, request,Blueprint
from app import create_app, db
from app.forms import LoginForm, WorkOrderForm, InspectionForm, AssetForm
from app.models import User, Asset, WorkOrder, Inspection
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

views=Blueprint('views',__name__)
@create_app.route('/')
@login_required
def dashboard():
    return render_template('dashboard.html')

@create_app.route('/work_orders', methods=['GET', 'POST'])
@login_required
def work_orders():
    form = WorkOrderForm()
    if form.validate_on_submit():
        work_order = WorkOrder(
            asset_id=form.asset_id.data,
            description=form.description.data,
            priority=form.priority.data,
            status=form.status.data,
            assigned_to=form.assigned_to.data,
            start_date=form.start_date.data,
            end_date=form.end_date.data,
            inspection_id=form.inspection_id.data
        )
        db.session.add(work_order)
        db.session.commit()
        flash('Work order created successfully.')
        return redirect(url_for('work_orders'))
    work_orders = WorkOrder.query.all()
    return render_template('work_orders.html', form=form, work_orders=work_orders)

@create_app.route('/inspections', methods=['GET', 'POST'])
@login_required
def inspections():
    form = InspectionForm()
    if form.validate_on_submit():
        inspection = Inspection(
            asset_id=form.asset_id.data,
            inspector=form.inspector.data,
            inspection_date=form.inspection_date.data,
            condition=form.condition.data,
            notes=form.notes.data
        )
        db.session.add(inspection)
        db.session.commit()
        flash('Inspection created successfully.')
        return redirect(url_for('inspections'))
    inspections = Inspection.query.all()
    return render_template('inspections.html', form=form, inspections=inspections)

@create_app.route('/assets', methods=['GET', 'POST'])
@login_required
def assets():
    form = AssetForm()
    if form.validate_on_submit():
        asset = Asset(
            asset_type=form.asset_type.data,
            location=form.location.data,
            condition=form.condition.data,
            last_inspection_date=form.last_inspection_date.data
        )
        db.session.add(asset)
        db.session.commit()
        flash('Asset created successfully.')
        return redirect(url_for('assets'))
    assets = Asset.query.all()
    return render_template('assets.html', form=form, assets=assets)

@create_app.route('/reports')
@login_required
def reports():
    return render_template('reports.html')

@create_app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and check_password_hash(user.password_hash, form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('dashboard'))
        flash('Invalid username or password.')
    return render_template('login.html', form=form)

@create_app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))