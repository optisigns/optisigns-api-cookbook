# listAllDevices

Retrieves all devices accessible to the authenticated user.

## Usage

```ts
import { listAllDevices } from "./listAllDevices";

async function example() {
  try {
    const devices = await listAllDevices("YOUR_API_KEY");
    console.log("All Devices:", devices);
  } catch (error) {
    console.error(error);
  }
}
```
