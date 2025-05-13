routes = [
    {
        "path": "/",
        "title": "首页",
        "icon": "home",
        "viewpath": "",
        "view": "",
    },
    {
        "path": "/tools",
        "title": "工具",
        "icon": "construction",
        "submenus": [
            {"path": "/apitest", "title": "Api测试", "viewpath": "", "view": ""},
            {"path": "/jsonformat", "title": "Json格式化", "viewpath": "tools.json_format_view", "view": "JsonFormatView"},
            {"path": "/process", "title": "进程管理", "viewpath": "", "view": ""},
            {"path": "/service", "title": "服务管理", "viewpath": "", "view": ""},
        ],
    },
    {
        "path": "/users",
        "title": "用户管理",
        "icon": "group",
        "submenus": [
            {"path": "/list", "title": "用户列表", "viewpath": "", "view": ""},
            {"path": "/roles", "title": "角色管理", "viewpath": "", "view": ""},
            {"path": "/permissions", "title": "权限设置", "viewpath": "", "view": ""},
        ],
    },
    {
        "path": "/settings",
        "title": "系统设置",
        "icon": "settings",
        "submenus": [
            {"path": "/basic", "title": "基本设置", "viewpath": "", "view": ""},
            {"path": "/network", "title": "网络设置", "viewpath": "", "view": ""},
            {"path": "/security", "title": "安全设置", "viewpath": "", "view": ""},
        ],
    },
]
