# -*- coding: utf-8 -*-
from django import forms
from django.utils import timezone

class OrderForm(forms.Form):

	name = forms.CharField()
	last_name = forms.CharField(required=False)
	phone = forms.CharField()
	buying_type = forms.ChoiceField(widget=forms.Select(), choices=([("self", "Самовывоз"),("delivery", "Доставка")]))
	delivery_date = forms.DateField(widget=forms.SelectDateWidget(), initial=timezone.now())
	address = forms.CharField(required=False)
	comments = forms.CharField(widget=forms.Textarea, required=False)


	def __init__(self, *args, **kwargs):
		super(OrderForm, self).__init__(*args, **kwargs)
		self.fields['name'].label = 'Имя'
		self.fields['last_name'].label = 'Фамилия'
		self.fields['phone'].label = 'Контактный телефон'
		self.fields['phone'].help_text = 'Пожалуйста, указывайте реальный номер телефона, по которому с Вами можно связаться'
		self.fields['buying_type'].label = 'Способ получения'
		self.fields['address'].label = 'Адрес доставки'
		self.fields['address'].help_text = '*Обязательно указывайте город!'
		self.fields['comments'].label = 'Комментарии к заказу'
		self.fields['delivery_date'].label = 'Дата доставки'
		self.fields['delivery_date'].help_text = 'Доставка производится на следущий день после оформления заказа. Менеджер с Вами предварительно свяжется!'
