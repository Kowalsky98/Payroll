### Estructura Completa del Módulo de Odoo (Payroll)

#### Archivos Base
- `pyproject.toml`
- `README.rst`
- `__init__.py`
- `__manifest__.py`

---

### Carpetas y Archivos

#### 1. **`data/`**
   - `hr_payroll_data.xml`
   - `hr_payroll_sequence.xml`

#### 2. **`demo/`**
   - `hr_payroll_demo.xml`

#### 3. **`i18n/`**
   - Archivos de traducción: `af.po`, `es.po`, `fr.po`, etc.
   - `payroll.pot`

#### 4. **`models/`**
   - `base_browsable.py`
   - `hr_contract.py`
   - `hr_contribution_register.py`
   - `hr_employee.py`
   - `hr_leave_type.py`
   - `hr_payroll_structure.py`
   - `hr_payslip.py`
   - `hr_payslip_input.py`
   - `hr_payslip_line.py`
   - `hr_payslip_run.py`
   - `hr_payslip_worked_days.py`
   - `hr_rule_input.py`
   - `hr_salary_rule.py`
   - `hr_salary_rule_category.py`
   - `res_config_settings.py`
   - `__init__.py`

#### 5. **`report/`**
   - `report.xml`
   - `report_contribution_register.py`
   - `report_payslip_details.py`
   - `__init__.py`

#### 6. **`security/`**
   - `hr_payroll_security.xml`
   - `ir.model.access.csv`

#### 7. **`static/`**
   - **`description/`:**
     - `icon.png`
     - `icon.svg`
     - `index.html`
   - **`img/`:**
     - `hr_employee_payroll-image.jpg`

#### 8. **`tests/`**
   - `common.py`
   - `test_browsable_object.py`
   - `test_hr_payroll_cancel.py`
   - `test_hr_payslip_change_state.py`
   - `test_hr_payslip_worked_days.py`
   - `test_hr_salary_rule.py`
   - `test_payslip_flow.py`
   - `__init__.py`

#### 9. **`views/`**
   - `hr_contract_views.xml`
   - `hr_contribution_register_views.xml`
   - `hr_employee_views.xml`
   - `hr_payroll_structure_views.xml`
   - `hr_payslip_line_views.xml`
   - `hr_payslip_run_views.xml`
   - `hr_payslip_views.xml`
   - `hr_salary_rule_category_views.xml`
   - `hr_salary_rule_views.xml`
   - `menus.xml`
   - `report_contributionregister.xml`
   - `report_payslip.xml`
   - `report_payslipdetails.xml`
   - `res_config_settings_views.xml`

#### 10. **`wizard/`**
   - `hr_payroll_contribution_register_report.py`
   - `hr_payroll_contribution_register_report_views.xml`
   - `hr_payroll_payslips_by_employees.py`
   - `hr_payroll_payslips_by_employees_views.xml`
   - `hr_payroll_send_email.xml`
   - `hr_payslip_change_state.py`
   - `hr_payslip_change_state_view.xml`
   - `__init__.py`