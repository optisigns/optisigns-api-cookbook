# pairDevice

Pairs a new device (via pairing code) to a specified team.

## Usage

```ts
import { pairDevice } from "./pairDevice";

async function example() {
  try {
    const newDevice = await pairDevice(
      "YOUR_API_KEY",
      "ABCD-1234",
      "/Lobby",
      "TEAM_ID"
    );
    console.log("Paired Device:", newDevice);
  } catch (error) {
    console.error(error);
  }
}
```
