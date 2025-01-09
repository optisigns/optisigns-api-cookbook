# moveDeviceToFolder

Moves a device to a different folder in the OptiSigns hierarchy.

## Usage

```ts
import { moveDeviceToFolder } from "./moveDeviceToFolder";

async function example() {
  try {
    const updatedDevice = await moveDeviceToFolder(
      "YOUR_API_KEY",
      "DEVICE_ID",
      "/Marketing/Displays",
      "TEAM_ID"
    );
    console.log("Moved Device:", updatedDevice);
  } catch (error) {
    console.error(error);
  }
}
```
