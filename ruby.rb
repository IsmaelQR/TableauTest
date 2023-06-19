require 'jwt'
require 'securerandom'

CONNECTED_APP_SECRET_ID = '981a4b50-f4ff-42fd-8993-532773439a0f'.freeze
CONNECTED_APP_SECRET_VALUE = 'hnOFFl9e84SrA6N/8MWtOostRITqdLnPxLFlhgZnKzI='.freeze
CONNECTED_APP_CLIENT_ID = '187d3cf1-7230-4550-af40-aa041f0d40cf'.freeze

def bearer_token_payload
  {
    iss: CONNECTED_APP_CLIENT_ID,
    sub: 'daniel.rivas@bebraven.org',
    aud: 'tableau',
    exp: Time.now.to_i + 300,
    jti: SecureRandom.uuid,
    scp: ['tableau:views:embed', 'tableau:metrics:embed'],
    Region: 'East'
  }
end

def token
  JWT.encode(bearer_token_payload, CONNECTED_APP_SECRET_VALUE, 'HS256', iss: CONNECTED_APP_CLIENT_ID, kid: CONNECTED_APP_SECRET_ID)
end

# Imprimir el token generado
print token

