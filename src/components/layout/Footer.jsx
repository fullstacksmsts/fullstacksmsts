import React from 'react';
import { Link } from 'react-router-dom';

const Footer = () => {
  return (
    <footer className="bg-[var(--primary-blue)] text-white">
      <div className="container mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
          {/* Company Info */}
          <div>
            <h3 className="text-lg font-bold mb-4">FullStack SMSTS</h3>
            <p className="mb-4">
              Providing CITB-accredited SMSTS courses with a 98% pass rate and competitive pricing.
            </p>
            <div className="flex items-center">
              <span className="bg-[var(--orange-accent)] px-2 py-1 rounded text-sm">
                CITB Accredited
              </span>
            </div>
          </div>
          
          {/* Quick Links */}
          <div>
            <h3 className="text-lg font-bold mb-4">Quick Links</h3>
            <ul className="space-y-2">
              <li>
                <Link to="/" className="hover:text-[var(--orange-accent)]">
                  Home
                </Link>
              </li>
              <li>
                <Link to="/courses" className="hover:text-[var(--orange-accent)]">
                  SMSTS Courses
                </Link>
              </li>
              <li>
                <Link to="/blog" className="hover:text-[var(--orange-accent)]">
                  Blog
                </Link>
              </li>
              <li>
                <Link to="/contact" className="hover:text-[var(--orange-accent)]">
                  Contact Us
                </Link>
              </li>
            </ul>
          </div>
          
          {/* Course Types */}
          <div>
            <h3 className="text-lg font-bold mb-4">Course Types</h3>
            <ul className="space-y-2">
              <li>
                <Link to="/courses/weekend" className="hover:text-[var(--orange-accent)]">
                  Weekend Courses
                </Link>
              </li>
              <li>
                <Link to="/courses/weekday" className="hover:text-[var(--orange-accent)]">
                  Weekday Courses
                </Link>
              </li>
              <li>
                <Link to="/courses/online" className="hover:text-[var(--orange-accent)]">
                  Online Courses
                </Link>
              </li>
              <li>
                <Link to="/courses/refresher" className="hover:text-[var(--orange-accent)]">
                  Refresher Courses
                </Link>
              </li>
            </ul>
          </div>
          
          {/* Contact Info */}
          <div>
            <h3 className="text-lg font-bold mb-4">Contact Us</h3>
            <ul className="space-y-2">
              <li className="flex items-center">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 mr-2" viewBox="0 0 20 20" fill="currentColor">
                  <path d="M2 3a1 1 0 011-1h2.153a1 1 0 01.986.836l.74 4.435a1 1 0 01-.54 1.06l-1.548.773a11.037 11.037 0 006.105 6.105l.774-1.548a1 1 0 011.059-.54l4.435.74a1 1 0 01.836.986V17a1 1 0 01-1 1h-2C7.82 18 2 12.18 2 5V3z" />
                </svg>
                <a href="tel:01234567890">01234 567 890</a>
              </li>
              <li className="flex items-center">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 mr-2" viewBox="0 0 20 20" fill="currentColor">
                  <path d="M2.003 5.884L10 9.882l7.997-3.998A2 2 0 0016 4H4a2 2 0 00-1.997 1.884z" />
                  <path d="M18 8.118l-8 4-8-4V14a2 2 0 002 2h12a2 2 0 002-2V8.118z" />
                </svg>
                <a href="mailto:info@fullstacksmsts.co.uk">info@fullstacksmsts.co.uk</a>
              </li>
              <li className="mt-4">
                <Link 
                  to="/book-course" 
                  className="bg-[var(--cta-orange)] hover:bg-[var(--orange-accent)] text-white px-4 py-2 rounded-lg inline-block transition duration-150"
                >
                  Book Now
                </Link>
              </li>
            </ul>
          </div>
        </div>
        
        <div className="border-t border-gray-700 mt-8 pt-8 flex flex-col md:flex-row justify-between">
          <p>&copy; {new Date().getFullYear()} FullStack SMSTS. All rights reserved.</p>
          <div className="mt-4 md:mt-0 flex space-x-4">
            <Link to="/privacy-policy" className="hover:text-[var(--orange-accent)]">
              Privacy Policy
            </Link>
            <Link to="/terms-of-service" className="hover:text-[var(--orange-accent)]">
              Terms of Service
            </Link>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
