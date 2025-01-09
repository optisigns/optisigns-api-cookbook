# assignOperationalSchedule

Assigns an operational schedule to a device.

## Usage

```ts
import { assignOperationalSchedule } from "./assignOperationalSchedule";

async function example() {
  try {
    const updatedDevice = await assignOperationalSchedule(
      "YOUR_API_KEY",
      "DEVICE_ID",
      "SCHEDULE_OPS_ID",
      "TEAM_ID"
    );
    console.log("Schedule Assigned:", updatedDevice);
  } catch (error) {
    console.error(error);
  }
}
```
