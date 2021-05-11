## Sagemaker Edge Agent To Pelion API (seatpapi)

This python package simplifies the Data Scientist's job of accessing the Sagemaker Edge Agent running on their Pelion Edge enabled gateway.

### Allocation

To invoke an instance of this API:
	
	# Required import
	from seatpapi import PelionAPI
	
	# Invoke constructor with Pelion API Key, Pelion GW Device ID
	# You can also optionally specify the Pelion API endpoint you want to use
	#
	api = PelionAPI(api_key='<ak_xxxx>', 
								 device_id='<pelion_gw_device_id>', 
								 api_endpoint='api.us-east-1.mbedcloud.com')
		
		
### Supported Commands

The following commands are supported in this packages

#### Get Configuration

	api.pelion_get_config()
	
	This call returns a JSON with the current Edge Device representing the 
	Sagemaker service's configuration
	
#### Set Configuration

	api.pelion_set_config({'foo':'bar'})
	
	This call updates or adds key/values to the current Edge Device's configuration
	
#### List Models

	api.pelion_list_models()
	
	This call returns a JSON outlining all of the loaded models
	
#### Load Model

	api.pelion_load_model('model-name','compiled-model-x.y.tar.gz')
	
	This call loads up the requested Sagemaker-compiled model whose compiled 
	contents are located within the S3 bucket defined in the configuration
	and utilized by the Sagemaker service
	
#### Unload Model

	api.pelion_unload_model('model-name')
	
	This call unloads the loaded model referenced by the name 'model-name'
	
#### Predict

	api.pelion_predict('model-name','s3:///input.data', 's3:///prediction_result.data')
	
	This call invokes the model prediction using the specified input.data file that is
	configured to be pulled from the Sagemaker S3 bucket (per configuration). The output
	result from the prediction will be stored in a file that will be saved to the same
	directory in the S3 bucket. 
	
	In addition to S3 bucket support, you can locally reference input/output requirements
	using the "file:///" protocol - in this case the Sagemaker Edge Agent working directory
	on the Pelion Edge Gateway will contain the specified files. 
	
#### Last Command Result

	api.pelion_last_cmd_result()
	
	This call simply returns the last invocation result. In cases where predictions take
	a long time to complete, this call may be used in a polling situation to determine
	when the prediction operation has completed. 

