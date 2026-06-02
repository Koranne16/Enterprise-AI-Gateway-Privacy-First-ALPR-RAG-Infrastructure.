import json
import hashlib

def sanitize_telemetry_payload(raw_payload: str) -> str:
    """
    Enterprise AI Gateway Middleware:
    Intercepts legacy ALPR telemetry payloads and masks PII (License Plate, GPS)
    prior to transmission to external frontier LLMs (Claude 3.5 / GPT-4).
    Ensures zero-trust isolation and strict DOT privacy compliance.
    """
    try:
        data = json.loads(raw_payload)
        
        # 1. Mask License Plate: Use one-way SHA-256 hash
        # Allows tracking of duplicate vehicles without exposing the actual plate
        if 'license_plate' in data:
            hashed_plate = hashlib.sha256(data['license_plate'].encode()).hexdigest()
            data['license_plate'] = f"REDACTED_{hashed_plate[:8]}"
            
        # 2. Obfuscate Location Data: Strip exact GPS for regional grid compliance
        if 'gps_coordinates' in data:
            data['gps_coordinates'] = "REDACTED_REGIONAL_ZONE"
            
        # 3. Strip driver demographic data if present in legacy payload
        if 'registered_owner_data' in data:
            del data['registered_owner_data']
            
        return json.dumps(data, indent=2)

    except Exception as e:
        # Fail secure: If payload parsing fails, block transmission entirely
        return json.dumps({"error": "Payload sanitization failed. Transmission blocked."})
