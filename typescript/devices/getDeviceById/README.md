# getDeviceById

Retrieves a device by its unique ID.

## Usage

```ts
import { getDeviceById } from "./getDeviceById";

async function example() {
  try {
    const device = await getDeviceById("YOUR_API_KEY", "DEVICE_ID");
    console.log("Device Details:", device);
  } catch (error) {
    console.error(error);
  }
}
```
