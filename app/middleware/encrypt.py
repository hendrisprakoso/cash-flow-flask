import hashlib, base64


def encryptPassword(value):
	
	if value in ('', None):
		return value
	
	# hashing with base64
	b_enc_base64 = base64.b64encode(bytes(value, 'utf-8')) 
	encrypt_str = b_enc_base64.decode('utf-8') 

	# hashing from base64 -> md5
	encrypt_md5 = hashlib.md5(encrypt_str.encode())

	return encrypt_md5.hexdigest()
