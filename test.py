import importlib

if __name__ == "__main__":
    mod = importlib.import_module("app.view.tools.json_format_view")
    print(mod)
    print(mod.JsonFormatView().build())
