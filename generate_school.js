const lodash = require("lodash");
const schoolid = require("@jx3box/jx3box-data/data/xf/schoolid.json");
const kungfuid = require("@jx3box/jx3box-data/data/martial/kungfuid.json");
const xfid = require("@jx3box/jx3box-data/data/xf/xfid.json");
const mount_group = require("@jx3box/jx3box-data/data/xf/mount_group.json");
const forceid = require("@jx3box/jx3box-data/data/xf/forceid.json");
const colors = require("@jx3box/jx3box-data/data/xf/colors.json");
const icons = require("@jx3box/jx3box-data/data/xf/std/skill_id_icon.json");
const relation = require("@jx3box/jx3box-data/data/xf/relation.json");
const fs = require("fs");

const result = {};

result["school"] = lodash.mapValues(lodash.invert(schoolid), Number);
result["kungfu"] = lodash.mapValues(lodash.invert(kungfuid), Number);
result["mount"] = lodash.mapValues(lodash.invert(xfid), Number);
result["mountg"] = mount_group.mount_group;
result["mountg"]["奶妈"] = result["mountg"]["治疗"];
delete result["mountg"]["治疗"];

result["forceid"] = lodash.mapValues(lodash.invert(forceid), Number);
result["color"] = colors.colors_by_school_name;
for (const school in result["color"]) {
    result["color"][result["school"][school]] = result["color"][school];
    delete result["color"][school];
}

result["detail"] = Object.keys(result["mount"]).reduce((acc, key) => {
    const detail = {
        name: key,
        color: colors.colors_by_mount_name[key],
        id: result["mount"][key],
        icon: icons[result["mount"][key]]?.[0] || 0,
        force: result["forceid"][relation.mount_belong_school[key]],
        school: result["school"][relation.mount_belong_school[key]],
    };
    acc[key] = detail;
    return acc;
}, {});

fs.writeFileSync("school.json", JSON.stringify(result, null, 4));
