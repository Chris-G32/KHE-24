import './Inputs.css'
import SearchIcon from '@mui/icons-material/Search';

function SearchBar({ placeholder, value, onChange, onSubmit, style }) {
    return (
        <form className='search-bar' onSubmit={onSubmit} style={style}>
            <input type="text" placeholder={placeholder} value={value} onChange={onChange} style={{ color: 'var(--text-dark)' }} />
            <button type='submit'><SearchIcon /></button>
        </form>
    )
}

function InputField({ type, placeholder, value, onChange}) {
    return (
        <input className='input-field' type={type} placeholder={placeholder} value={value} onChange={onChange} style={{ color: 'var(--text-dark)' }} />
    )
}

export {
    SearchBar,
    InputField
}