# getDeviceByName

Searches for devices by a specific name.

## Usage

```ts
import { getDeviceByName } from "./getDeviceByName";

async function example() {
  try {
    const devices = await getDeviceByName("YOUR_API_KEY", "Lobby Display");
    console.log("Matching Devices:", devices);
  } catch (error) {
    console.error(error);
  }
}
```
