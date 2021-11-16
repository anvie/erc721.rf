pragma solidity ^0.8.0;

// SPDX-License-Identifier: MIT

import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "./HasAdmin.sol";
import "./HasRoot.sol";

contract $name_pascal_case$ is
    ERC721,
    HasRoot,
    HasAdmin
{
    using SafeMath for uint256;
    // using SafeMath for uint32;
    using Counters for Counters.Counter;

    Counters.Counter private _idGen;

    string public baseTokenURI;

    event ItemMinted(uint256 indexed tokenId);

    constructor()
        ERC721("$name$", "$param.token_code$")
    {
        _setRoot(_msgSender());
        _setAdmin(_msgSender());
    }

    modifier onlyAdminOrOwner() {
        require(
            _isAdmin(_msgSender()) || _isRoot(_msgSender()),
            "Only root or admin can set daily aging rate"
        );
        _;
    }

    function changeRoot(address newRoot) external onlyRoot {
        _setRoot(newRoot);
    }

    function changeAdmin(address newAdmin) external onlyRoot {
        _setAdmin(newAdmin);
    }

    function mint(address to) external returns(uint256) {
        uint256 tokenId = _idGen.current();
        _safeMint(to, tokenId);
        _idGen.increment();
        emit ItemMinted(tokenId);
        return tokenId;
    }


    function _baseURI() internal view virtual override returns (string memory) {
        return baseTokenURI;
    }

    function setBaseURI(string memory baseURI) public onlyRoot {
        baseTokenURI = baseURI;
    }
}
