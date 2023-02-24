#This unit test checks the prediction function for the probability to predict class 1

import ast
import json
import streamlit as st
import urllib.request

def test_prediction():
    def prediction(input_data):    
        data =  {
        "input_data": {
            "columns": [
                "AMT_ANNUITY",
                "AMT_CREDIT",
                "AMT_GOODS_PRICE",
                "AMT_INCOME_TOTAL",
                "AMT_REQ_CREDIT_BUREAU_DAY",
                "AMT_REQ_CREDIT_BUREAU_HOUR",
                "AMT_REQ_CREDIT_BUREAU_MON",
                "AMT_REQ_CREDIT_BUREAU_QRT",
                "AMT_REQ_CREDIT_BUREAU_WEEK",
                "AMT_REQ_CREDIT_BUREAU_YEAR",
                "ANNUITY_INCOME_PERC",
                "APPROVED_AMT_ANNUITY_MAX",
                "APPROVED_AMT_ANNUITY_MEAN",
                "APPROVED_AMT_ANNUITY_MIN",
                "APPROVED_AMT_APPLICATION_MAX",
                "APPROVED_AMT_APPLICATION_MEAN",
                "APPROVED_AMT_APPLICATION_MIN",
                "APPROVED_AMT_CREDIT_MAX",
                "APPROVED_AMT_CREDIT_MEAN",
                "APPROVED_AMT_CREDIT_MIN",
                "APPROVED_AMT_DOWN_PAYMENT_MAX",
                "APPROVED_AMT_DOWN_PAYMENT_MEAN",
                "APPROVED_AMT_DOWN_PAYMENT_MIN",
                "APPROVED_AMT_GOODS_PRICE_MAX",
                "APPROVED_AMT_GOODS_PRICE_MEAN",
                "APPROVED_AMT_GOODS_PRICE_MIN",
                "APPROVED_APP_CREDIT_PERC_MAX",
                "APPROVED_APP_CREDIT_PERC_MEAN",
                "APPROVED_APP_CREDIT_PERC_MIN",
                "APPROVED_CNT_PAYMENT_MEAN",
                "APPROVED_CNT_PAYMENT_SUM",
                "APPROVED_DAYS_DECISION_MAX",
                "APPROVED_DAYS_DECISION_MEAN",
                "APPROVED_DAYS_DECISION_MIN",
                "APPROVED_HOUR_APPR_PROCESS_START_MAX",
                "APPROVED_HOUR_APPR_PROCESS_START_MEAN",
                "APPROVED_HOUR_APPR_PROCESS_START_MIN",
                "APPROVED_RATE_DOWN_PAYMENT_MAX",
                "APPROVED_RATE_DOWN_PAYMENT_MEAN",
                "APPROVED_RATE_DOWN_PAYMENT_MIN",
                "BURO_AMT_CREDIT_SUM_DEBT_MAX",
                "BURO_AMT_CREDIT_SUM_DEBT_MEAN",
                "BURO_AMT_CREDIT_SUM_DEBT_SUM",
                "BURO_AMT_CREDIT_SUM_LIMIT_SUM",
                "BURO_AMT_CREDIT_SUM_MAX",
                "BURO_AMT_CREDIT_SUM_MEAN",
                "BURO_AMT_CREDIT_SUM_OVERDUE_MEAN",
                "BURO_AMT_CREDIT_SUM_SUM",
                "BURO_CNT_CREDIT_PROLONG_SUM",
                "BURO_CREDIT_DAY_OVERDUE_MAX",
                "BURO_CREDIT_DAY_OVERDUE_MEAN",
                "BURO_DAYS_CREDIT_ENDDATE_MAX",
                "BURO_DAYS_CREDIT_ENDDATE_MEAN",
                "BURO_DAYS_CREDIT_ENDDATE_MIN",
                "BURO_DAYS_CREDIT_MAX",
                "BURO_DAYS_CREDIT_MEAN",
                "BURO_DAYS_CREDIT_MIN",
                "BURO_DAYS_CREDIT_UPDATE_MEAN",
                "BURO_MONTHS_BALANCE_SIZE_SUM",
                "CNT_CHILDREN",
                "CNT_FAM_MEMBERS",
                "CODE_GENDER",
                "DAYS_BIRTH",
                "DAYS_EMPLOYED",
                "DAYS_EMPLOYED_PERC",
                "DAYS_ID_PUBLISH",
                "DAYS_LAST_PHONE_CHANGE",
                "DAYS_REGISTRATION",
                "DEF_30_CNT_SOCIAL_CIRCLE",
                "DEF_60_CNT_SOCIAL_CIRCLE",
                "EMERGENCYSTATE_MODE",
                "EXT_SOURCE_2",
                "EXT_SOURCE_3",
                "FLAG_CONT_MOBILE",
                "FLAG_DOCUMENT_10",
                "FLAG_DOCUMENT_11",
                "FLAG_DOCUMENT_12",
                "FLAG_DOCUMENT_13",
                "FLAG_DOCUMENT_14",
                "FLAG_DOCUMENT_15",
                "FLAG_DOCUMENT_16",
                "FLAG_DOCUMENT_17",
                "FLAG_DOCUMENT_18",
                "FLAG_DOCUMENT_19",
                "FLAG_DOCUMENT_2",
                "FLAG_DOCUMENT_20",
                "FLAG_DOCUMENT_21",
                "FLAG_DOCUMENT_3",
                "FLAG_DOCUMENT_4",
                "FLAG_DOCUMENT_5",
                "FLAG_DOCUMENT_6",
                "FLAG_DOCUMENT_7",
                "FLAG_DOCUMENT_8",
                "FLAG_DOCUMENT_9",
                "FLAG_EMAIL",
                "FLAG_EMP_PHONE",
                "FLAG_MOBIL",
                "FLAG_OWN_CAR",
                "FLAG_OWN_REALTY",
                "FLAG_PHONE",
                "FLAG_WORK_PHONE",
                "FONDKAPREMONT_MODE",
                "HOUR_APPR_PROCESS_START",
                "HOUSETYPE_MODE",
                "INCOME_CREDIT_PERC",
                "INCOME_PER_PERSON",
                "INSTAL_AMT_INSTALMENT_MAX",
                "INSTAL_AMT_INSTALMENT_MEAN",
                "INSTAL_AMT_INSTALMENT_SUM",
                "INSTAL_AMT_PAYMENT_MAX",
                "INSTAL_AMT_PAYMENT_MEAN",
                "INSTAL_AMT_PAYMENT_MIN",
                "INSTAL_AMT_PAYMENT_SUM",
                "INSTAL_COUNT",
                "INSTAL_DAYS_ENTRY_PAYMENT_MAX",
                "INSTAL_DAYS_ENTRY_PAYMENT_MEAN",
                "INSTAL_DAYS_ENTRY_PAYMENT_SUM",
                "INSTAL_DBD_MAX",
                "INSTAL_DBD_MEAN",
                "INSTAL_DBD_SUM",
                "INSTAL_DPD_MAX",
                "INSTAL_DPD_MEAN",
                "INSTAL_DPD_SUM",
                "INSTAL_NUM_INSTALMENT_VERSION_NUNIQUE",
                "INSTAL_PAYMENT_DIFF_MAX",
                "INSTAL_PAYMENT_DIFF_MEAN",
                "INSTAL_PAYMENT_DIFF_SUM",
                "INSTAL_PAYMENT_DIFF_VAR",
                "INSTAL_PAYMENT_PERC_MAX",
                "INSTAL_PAYMENT_PERC_MEAN",
                "INSTAL_PAYMENT_PERC_SUM",
                "INSTAL_PAYMENT_PERC_VAR",
                "LIVE_CITY_NOT_WORK_CITY",
                "LIVE_REGION_NOT_WORK_REGION",
                "NAME_CONTRACT_TYPE",
                "NAME_EDUCATION_TYPE",
                "NAME_FAMILY_STATUS",
                "NAME_HOUSING_TYPE",
                "NAME_INCOME_TYPE",
                "NAME_TYPE_SUITE",
                "OBS_30_CNT_SOCIAL_CIRCLE",
                "OBS_60_CNT_SOCIAL_CIRCLE",
                "OCCUPATION_TYPE",
                "ORGANIZATION_TYPE",
                "PAYMENT_RATE",
                "POS_COUNT",
                "POS_MONTHS_BALANCE_MAX",
                "POS_MONTHS_BALANCE_MEAN",
                "POS_MONTHS_BALANCE_SIZE",
                "POS_SK_DPD_DEF_MAX",
                "POS_SK_DPD_DEF_MEAN",
                "POS_SK_DPD_MAX",
                "POS_SK_DPD_MEAN",
                "PREV_AMT_ANNUITY_MAX",
                "PREV_AMT_ANNUITY_MEAN",
                "PREV_AMT_ANNUITY_MIN",
                "PREV_AMT_APPLICATION_MAX",
                "PREV_AMT_APPLICATION_MEAN",
                "PREV_AMT_APPLICATION_MIN",
                "PREV_AMT_CREDIT_MAX",
                "PREV_AMT_CREDIT_MEAN",
                "PREV_AMT_CREDIT_MIN",
                "PREV_AMT_DOWN_PAYMENT_MAX",
                "PREV_AMT_DOWN_PAYMENT_MEAN",
                "PREV_AMT_DOWN_PAYMENT_MIN",
                "PREV_AMT_GOODS_PRICE_MAX",
                "PREV_AMT_GOODS_PRICE_MEAN",
                "PREV_AMT_GOODS_PRICE_MIN",
                "PREV_APP_CREDIT_PERC_MAX",
                "PREV_APP_CREDIT_PERC_MEAN",
                "PREV_APP_CREDIT_PERC_MIN",
                "PREV_CNT_PAYMENT_MEAN",
                "PREV_CNT_PAYMENT_SUM",
                "PREV_DAYS_DECISION_MAX",
                "PREV_DAYS_DECISION_MEAN",
                "PREV_DAYS_DECISION_MIN",
                "PREV_HOUR_APPR_PROCESS_START_MAX",
                "PREV_HOUR_APPR_PROCESS_START_MEAN",
                "PREV_HOUR_APPR_PROCESS_START_MIN",
                "PREV_RATE_DOWN_PAYMENT_MAX",
                "PREV_RATE_DOWN_PAYMENT_MEAN",
                "PREV_RATE_DOWN_PAYMENT_MIN",
                "REGION_POPULATION_RELATIVE",
                "REGION_RATING_CLIENT",
                "REGION_RATING_CLIENT_W_CITY",
                "REG_CITY_NOT_LIVE_CITY",
                "REG_CITY_NOT_WORK_CITY",
                "REG_REGION_NOT_LIVE_REGION",
                "REG_REGION_NOT_WORK_REGION",
                "SK_ID_CURR",
                "WALLSMATERIAL_MODE",
                "WEEKDAY_APPR_PROCESS_START",
                "index"
                ],
                "index": [0],
                "data": input_data
            }
        }

        body = str.encode(json.dumps(data))

        url = 'https://ocr-p7-api-mlflow-proba-qljnp.francecentral.inference.ml.azure.com/score' #API Endpoint in the cloud (Azure) opti proba weight class

        # Replace this with the primary/secondary key or AMLToken for the endpoint
        api_key = 'GBzKoAD0Bpc8rYUHS4iDwbHJrdwYCl4P' #Key for Predict_proba Model opti weight class
        if not api_key:
            raise Exception("A key should be provided to invoke the endpoint")

        # The azureml-model-deployment header will force the request to go to a specific deployment.
        # Remove this header to have the request observe the endpoint traffic rules
        headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key), 'azureml-model-deployment': 'lgbm-opti-class-weight-proba-2' }

        req = urllib.request.Request(url, body, headers)

        try:
            response = urllib.request.urlopen(req)
            
            result = response.read()
            print(result)
        except urllib.error.HTTPError as error:
            
            print("The request failed with status code: " + str(error.code))

            # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
            print(error.info())
            print(error.read().decode("utf8", 'ignore'))
        res_decoded = result.decode()
        res_str_list = ast.literal_eval(res_decoded)
        res_proba = res_str_list[0][1]
        return res_proba

    data_x = [
        [
            29569.5,
            552555,
            477000,
            99000,
            0,
            0,
            0,
            0,
            0,
            2,
            0.2986818181818181,
            14406.705,
            10183.64625,
            2420.775,
            118327.5,
            89218.125,
            22365,
            96795,
            66040.875,
            21789,
            45000,
            25360.875,
            2236.5,
            118327.5,
            89218.125,
            22365,
            1.5830546265328873,
            1.31453514100058,
            1.026435357290376,
            8,
            32,
            -397,
            -1569.5,
            -2643,
            14,
            11.75,
            10,
            0.4222550418864411,
            0.2585987452671526,
            0.1013819407788314,
            0,
            0,
            0,
            0,
            54591.3,
            53872.942500000005,
            0,
            215491.77,
            0,
            0,
            0,
            -463,
            -1325.5,
            -2165,
            -646,
            -1783.75,
            -2379,
            -1543.75,
            0,
            1,
            3,
            0,
            -15378,
            -2843,
            0.1848744960332943,
            -4400,
            -397,
            -5933,
            0,
            0,
            1,
            0.7323616761098093,
            0.7407990879702335,
            1,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            1,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            1,
            1,
            1,
            0,
            0,
            0,
            3,
            12,
            1,
            0.1791676846648749,
            33000,
            14410.935,
            9283.13578125,
            297060.345,
            14410.935,
            9283.13578125,
            2393.91,
            297060.345,
            32,
            -235,
            -1554.34375,
            -49739,
            19,
            8.15625,
            261,
            0,
            0,
            0,
            1,
            0,
            0,
            0,
            0,
            1,
            1,
            32,
            0,
            0,
            0,
            0,
            4,
            0,
            1,
            7,
            1,
            0,
            0,
            15,
            42,
            0.0535141298151315,
            36,
            -7,
            -50.833333333333336,
            36,
            0,
            0,
            0,
            0,
            14406.705,
            10183.64625,
            2420.775,
            118327.5,
            71374.5,
            0,
            96795,
            52832.7,
            0,
            45000,
            25360.875,
            2236.5,
            118327.5,
            89218.125,
            22365,
            1.5830546265328873,
            1.31453514100058,
            1.026435357290376,
            8,
            32,
            -110,
            -1277.6,
            -2643,
            15,
            12.4,
            10,
            0.4222550418864411,
            0.2585987452671526,
            0.1013819407788314,
            0.006207,
            2,
            2,
            0,
            0,
            0,
            0,
            106639,
            5,
            5,
            5675
        ]
        ]

    res = prediction(data_x)
    assert res == 0.02383658152180125, "Should be 0.02383658152180125"


if __name__ == "__main__":
    test_prediction()
    print("Everything passed")