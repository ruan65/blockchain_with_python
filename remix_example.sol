pragma solidity ^0.4.22;

contract Greeter {
    string public greeting;

    function Greeter() public {
        greeting = "Hello"
    }

    function setGreeting(string _greeting) {
        greeting = _greeting;
    }

    function greet() view public returns (string) {
        ret  greeting;
    }
}