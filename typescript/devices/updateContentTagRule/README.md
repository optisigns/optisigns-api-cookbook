# updateContentTagRule

Updates the content tag rule on a device.

## Usage

```ts
import { updateContentTagRule } from "./updateContentTagRule";

async function example() {
  try {
    const updatedDevice = await updateContentTagRule(
      "YOUR_API_KEY",
      "DEVICE_ID",
      "CONTENT_TAG_RULE_ID",
      "TEAM_ID"
    );
    console.log("Content Tag Rule Updated:", updatedDevice);
  } catch (error) {
    console.error(error);
  }
}
```
