import sys
import json
from card_provider import CardProvider, CardProviderSession

service_id = sys.argv[1]
secret_key = sys.argv[2]
user_id = sys.argv[3]

elems = [
    {
        "type": "div",
        "children": [
            {
                "type": "text_input",
                "name": "a",
                "label": "左值"
            },
            {
                "type": "text_input",
                "name": "b",
                "label": "右值"
            },
            {
                "type": "text_input",
                "name": "op",
                "label": "运算符"
            },
            {
                "type": "button",
                "name": "calc",
                "label": "计算"
            },
            {
                "type": "text_input",
                "name": "result",
                "label": "输出",
                "disabled": True
            }
        ]
    }
]

script = '''
let ret = {
    "set": {
        textFields: {
            result: "" + ({
                "+": (a, b) => a + b,
                "-": (a, b) => a - b,
                "*": (a, b) => a * b,
                "/": (a, b) => a / b
            })[window.executeParams.textFields.op.trim()](
                parseFloat(window.executeParams.textFields.a),
                parseFloat(window.executeParams.textFields.b)
            )
        }
    }
};
ret
'''

sess = CardProvider(service_id, secret_key).get_session(user_id)
sess.add_card(title = "计算器", elements = elems, script_code = script)
print("OK")
