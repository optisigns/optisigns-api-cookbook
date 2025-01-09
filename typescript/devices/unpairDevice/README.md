# unpairDevice

Unpairs (removes) a device from a specified team.

## Usage

```ts
import { unpairDevice } from "./unpairDevice";

async function example() {
  try {
    const wasUnpaired = await unpairDevice(
      "YOUR_API_KEY",
      "DEVICE_ID",
      "TEAM_ID"
    );
    console.log("Unpair Successful?", wasUnpaired);
  } catch (error) {
    console.error(error);
  }
}
```
