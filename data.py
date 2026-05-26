import random

politicians = [
    "teri leila",
    "miss kumari",
    "tere naam",
    "kali kursi"
]

companies = [
    "TechNova",
    "FutureX",
    "InfoCore",
    "SkyLabsX"
]

cities = [
    "Del",
    "Mum",
    "Bhl",
    "Pune",
    "Bang"
]

authors = [
    "mera Mehta",
    "tera Singh",
    "sabka Patel",
    "akela Sharma"
]

events = [
    "secret project",
    "innovation summit",
    "economic mission",
    "technology launch"
]

amounts = [
    "₹5 crore",
    "₹20 crore",
    "₹100 crore",
    "₹500 crore"
]

categories = [
    "Politics",
    "Technology",
    "Business",
    "Entertainment"
]

templates = {
    "Politics": [
        "{person} announces {amount} investment in {city}",
        "{person} launches new national policy in {city}"
    ],

    "Technology": [
        "{company} launches invisible smartphone in {city}",
        "{company} reveals AI-powered flying bike"
    ],

    "Business": [
        "{company} acquires startup for {amount}",
        "{company} opens mega office in {city}"
    ],

    "Entertainment": [
        "{person} signs blockbuster deal worth {amount}",
        "{person} announces surprise movie project"
    ]
}