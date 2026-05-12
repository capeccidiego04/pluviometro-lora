function decodeUplink(input) {
  var bytes = input.bytes;
  
  if(bytes[0]!==0x10){
    return { 
      data: { 
        key: "humm_diag", 
        type: "service_message", 
        header: bytes[0] 
      } 
    };
  }
  
  if (bytes.length < 5) return null;
  
  var pulses = bytes[1] | (bytes[2] << 8);
  
  var resolution = 0.254; 
  
  var rain_total = pulses * resolution;

  return {
    data: {
      key: "humm",
      status: bytes[0],
      cumulative_pulses: pulses,
      rain_mm: parseFloat(rain_total.toFixed(2)),
      battery_hex: bytes[4]
    }
  };
}
