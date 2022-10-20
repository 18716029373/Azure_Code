import datetime as _datetime

operator = 'bq2gcs'
file_format = 'csv'
backup_table_name = '{datalake_project_id}.{database_insight}.inline_' + _datetime.datetime.now().strftime("%Y%m%d%H%M%S")
backup_table_espiration_hours = 24
table_name='FNMS_Assets_epso'
file_uri = 'gs://prd-65343-datalake-bd-191397-dv1gait-bqdata-egr/EPSO_Split_2/Egress_EPSO'+'.csv'
custom_field_delimeter='|'


sql = """
Select
        asset_tag,
        model_category,
        u_sub_category,
        u_purchaser,
        u_corporate_unit,
        u_corporate_unit_last_level,
        cost_center,
        location,
        location_last_level,
        replace(replace(model,chr(10),''),chr(13),'/') as model,
        u_part_number,
        serial_number,
        asset_status,
        substatus,
        acquisition_method,
        delivery_date,
        u_exception_start_date,
        u_exception_end_date,
        u_requestor,
        u_exception_status,
        u_exception_sub_status,
        u_last_status_change,
        u_last_substatus_change,
        u_fixed_ip,
        u_pc_model_ref as u_pc_model,
        replace(u_project_id,'|','/') as u_project_id,
        u_multiple_asset_business_justification,
        replace(replace(replace(u_multiple_asset_other_valid_reason,chr(10),''),chr(13),'/'),'|','/') as u_multiple_asset_other_valid_reason,
        u_warranty_start_date,
        warranty_expiration,
        replace(replace(replace(u_wbs,chr(10),''),chr(13),'/'),'|','/') as u_wbs,
        u_project_name,
        assigned_to,
        install_date,
        u_legal_hold,
        missing_location,
        u_corporate_unit_1st_level,
        u_corporate_unit_3rd_level,
        u_multiple_asset_end_date,
        u_multiple_asset_start_date,
        u_days_since_state_change,
        u_corporate_unit_2nd_level,
        u_asset_id,
        sys_created_on,
        replace(replace(name,chr(10),''),chr(13),'/') as name,
        u_refresh_due_date,
        os,
        disk_space,
        ip_address,
        mac_address,
        os_service_pack,
        chassis_type,
        gl_account,
        cpu_speed,
        cpu_type,
        cpu_core_thread,
        ram,
        u_image_version,
        cpu_core_count,
        cpu_count,
        manufacturer,
        u_last_installed_patch_date,
        location_2nd_level,
        location_3rd_level,
        location_1st_level,
        email,
        assigneduser_userid,
        u_jobcddescr,
        employee_number,
        middle_name,
        last_name,
        u_lastdateworked,
        u_employmentstatusdescr,
        first_name,
        inventoryagentmanual,
        u_calculated_user,
        u_raw_last_logged_on_user,
        u_bitlocker_backup_to_ad_ds,
        u_bitlocker_c_conversion_status,
        u_bitlocker_c_encryption_method,
        u_bitlocker_service_started,
        u_bitlocker_require_backup_to_ad_ds,
        u_dlp_running,
        u_drive_encrypted_c,
        u_edpa_executable_found,
        u_edpa_service_started,
        u_edpa_service_state,
        u_edpa_service_status,
        u_pointsec_encryption_progress,
        u_pointsec_encryption_state,
        u_wdp_executable_found,
        u_wdp_service_started,
        u_wdp_service_state,
        u_available_updates,
        u_assigned_chassis_type,
        u_display_adapters,
        u_firewall_enabled_for_mac_only,
        u_hard_drives,
        u_inventory_connection,
        u_inventory_date,
        u_inventory_provided_within_30_days,
        u_network_cards,
        u_sockets,
        u_bitlocker_service_state,
        u_bitlocker_service_status,
        u_bitlocker_c_protection_status,
        u_days_since_inventory_received,
        u_inventory_received_since_status_change,
        u_sub_status,
        u_substate_reason,
        u_userobjectcd,
        u_eam_id
    FROM `prd-65343-datalake-bd-88394358.gait_191397_in.FNMS_Assets_epso_split_2` 
    """