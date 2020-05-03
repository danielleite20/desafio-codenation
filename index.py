import runRequest
import runPost
import runDecrypt
import hashlib

baseURL = 'https://api.codenation.dev/v1/challenge/dev-ps/'
token = '72d83b3cc03e8e410eeb77270c6e242b2308264f'

infoReceived = runRequest.request(baseURL, token)
textDecrypted = runDecrypt.decryptTextData(infoReceived['cifrado'],infoReceived['numero_casas'])

sha1Summary = hashlib.sha1(textDecrypted.encode()).hexdigest()
infoReceived['decifrado'] = textDecrypted
infoReceived['resumo_criptografico'] = sha1Summary


runPost.post(baseURL, infoReceived, token)