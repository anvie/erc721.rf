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

    uint256 public constant maxSupply = $param.max_supply$;

    Counters.Counter private _idGen;

    string public baseTokenURI;

    event ItemMinted(uint256 indexed tokenId);

    constructor(string memory _baseTokenURI, address root, address admin)
        ERC721("$name$", "$param.token_code$")
    {
        _setRoot(root);
        _setAdmin(admin);
        _idGen.reset();
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
        _idGen.increment();
        uint256 tokenId = _idGen.current();

        require(tokenId <= maxSupply, "max supply exceeded");

        _safeMint(to, tokenId);

        emit ItemMinted(tokenId);

        return tokenId;
    }

    function totalSupply() external view returns(uint256) {
        return _idGen.current();
    }

    function _baseURI() internal view virtual override returns (string memory) {
        return baseTokenURI;
    }

    function setBaseURI(string memory baseURI) public onlyRoot {
        baseTokenURI = baseURI;
    }
}
