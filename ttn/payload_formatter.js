function decodeUplink(input) {
  var bytes = input.bytes;
  
  if(bytes[0]!==0x10 && bytes[0]!=0x12){
    return { 
      data: { 
        key: "humm_diag", 
        type: "service_message", 
        header: bytes[0] 
      } 
    };
  }
  
  var rain_misurata = bytes[1] | (bytes[2] << 8);
  
  var rain_total = rain_misurata/10;

  return {
    data: {
      key: "humm",
      status: bytes[0],
      rain_mm: rain_total.toFixed(2),
      battery_hex: bytes[3]
    }
  };
}
